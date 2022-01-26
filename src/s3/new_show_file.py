# import os
# import requests
# import uuid
# import boto3
# from flask import Flask, jsonify, request, Response, stream_with_context
# from werkzeug.datastructures import Headers
# import json
# import re

# BUCKET = "netflix-clone-josino"

# def show_file():
#     storage = boto3.client('s3')
#     media_stream = storage.get_object(Bucket=BUCKET, Key=key)
#     full_content = media_stream['ContentLength']
#     headers = Headers()
#     status = 200
#     range_header = request.headers.get('Range', None)
#     if range_header:
#         byte_start, byte_end, length = get_byte_range(range_header)

#     headers.add('Content-Type', content_type)
#     headers.add('Content-Length', media_stream['ContentLength'])
#     response = Response(
#         stream_with_context(media_stream['Body'].iter_chunks()),
#         mimetype=content_type,
#         content_type=content_type,
#         headers=headers,
#         status=status
#         )
#     return response