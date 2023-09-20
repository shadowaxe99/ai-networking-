
from flask import Flask, request, jsonify
from .models.ai_agent import AIAgent
from .services.email_service import EmailService
from .services.zoom_service import ZoomService
from .services.networking_service import NetworkingService
from .services.search_service import SearchService

app = Flask(__name__)

@app.route('/network', methods=['POST'])
def network():
    data = request.get_json()
    user_email = data.get('user_email')
    ai_agent = AIAgent(user_email)
    email_service = EmailService(user_email)
    zoom_service = ZoomService(user_email)
    networking_service = NetworkingService(ai_agent, email_service, zoom_service)
    networking_service.network()
    return jsonify({'status': 'success'}), 200

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    user_email = data.get('user_email')
    ai_agent = AIAgent(user_email)
    search_service = SearchService(ai_agent)
    search_service.search()
    return jsonify({'status': 'success'}), 200

if __name__ == "__main__":
    app.run(debug=True)
