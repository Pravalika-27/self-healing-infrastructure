from flask import Flask, request, jsonify
import subprocess
import logging
from prometheus_client import Counter, start_http_server

app = Flask(__name__)
start_http_server(8000)

# Prometheus metrics
alerts_received = Counter('alerts_received_total', 'Total alerts received')
actions_executed = Counter('actions_executed_total', 'Total remediation actions executed')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    alerts_received.inc()
    
    for alert in data.get('alerts', []):
        if alert.get('status') == 'firing':
            alert_name = alert.get('labels', {}).get('alertname')
            if alert_name == 'NginxDown':
                logging.warning(f"NGINX down alert received: {alert}")
                try:
                    # Execute Ansible playbook to restart NGINX
                    result = subprocess.run(
                        ['ansible-playbook', '/app/restart_nginx.yml'],
                        capture_output=True, text=True
                    )
                    actions_executed.inc()
                    logging.info(f"Playbook execution result: {result.stdout}")
                    if result.returncode != 0:
                        logging.error(f"Playbook failed: {result.stderr}")
                except Exception as e:
                    logging.error(f"Error executing playbook: {e}")
    
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=5000)
