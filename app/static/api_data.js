define({
    "api": [
        {
            "type": "post",
            "url": "/upload/:uid",
            "title": "Upload user profile photo",
            "name": "Upload_Profile_Photo",
            "group": "FaceDetect_API",
            "description": "<p>Upload user profile photo</p>",
            "permission": [
                {
                    "name": "authenticated user"
                }
            ],
            "parameter": {
                "fields": {
                    "Parameter": [
                        {
                            "group": "Parameter",
                            "type": "String",
                            "optional": false,
                            "field": "file",
                            "description": "<p>User file mutipart/form-data</p>"
                        }
                    ]
                }
            },
            "success": {
                "fields": {
                    "Success 200": [
                        {
                            "group": "Success 200",
                            "type": "Number",
                            "optional": false,
                            "field": "status",
                            "description": "<p>HTTP 201 Created</p>"
                        },
                        {
                            "group": "Success 200",
                            "type": "Object[]",
                            "optional": false,
                            "field": "message",
                            "description": "<p>Success upload message</p>"
                        }
                    ]
                },
                "examples": [
                    {
                        "title": "Success-Response",
                        "content": "HTTP/1.1 201 Created\n{\n    \"status\": 201,\n    \"message\": {\n        \"uid\": 1507343002,\n        \"original\": \"http://localhost/images/1507343002/original.jpg\",\n        \"thumbnail\": \"http://localhost/images/1507343002/thumbnail.jpg\",\n        \"minify\": \"http://localhost/images/1507343002/minify.jpg\"\n    }\n}",
                        "type": "json"
                    }
                ]
            },
            "error": {
                "fields": {
                    "Error 4xx": [
                        {
                            "group": "Error 4xx",
                            "optional": false,
                            "field": "ImageUploaderError",
                            "description": "<p>Request does not match real req data</p>"
                        }
                    ]
                },
                "examples": [
                    {
                        "title": "ImageUploaderError",
                        "content": "HTTP/1.1 400 Bad Request\n{\n    \"status\": 400,\n    \"message\": \"Invalid request data\"\n}",
                        "type": "json"
                    }
                ]
            },
            "version": "0.0.0",
            "filename": "./server.py",
            "groupTitle": "FaceDetect_API",
            "sampleRequest": [
                {
                    "url": "http://localhost:88/upload/:uid"
                }
            ]
        }
    ]
});
