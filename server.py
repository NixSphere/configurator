#!/usr/bin/env python3

import os
from flask import Flask, jsonify, Response

app = Flask(__name__)

# Synchronous route that reads the configuration.nix file
@app.route('/')
def index():
    file_path = "/etc/nixos/configuration.nix"
    
    # Check if the file exists
    if os.path.exists(file_path):
        try:
            # Read the file synchronously
            with open(file_path, 'r') as f:
                data = f.read()
            return Response(data, mimetype="text/plain")
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
