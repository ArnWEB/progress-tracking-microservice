progress-tracking/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── progress_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── progress.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── progress_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── progress_service.py
│   ├── config.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── tests/
│   ├── __init__.py
│   └── test_progress_service.py
├── Dockerfile
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── secret.yaml
├── requirements.txt
└── README.md