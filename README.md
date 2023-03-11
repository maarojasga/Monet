# Challenge Monet
Prueba técnica Monet

## Requerimientos de Aplicación Django
1. Crear modelos de Student, Test, Question, Answer
2. Endpoint para identificar a un estudiante y devolver su respectivo JWT
3. Endpoint protegido para registrar las respuestas de un estudiante
4. Modificaciones al Django Admin para que un estudiante pueda ingresar al portal y solo
ver sus propias respuestas a los tests

## Instalación

### Windows
Crear entorno virtual
    python -m venv env

Activar entorno virtual
    env\Scripts\activate

Clonar repositorio
    https://github.com/maarojasga/Monet.git

Correr migraciones
    python manage.py makemigrations
    python manage.py migrate

Crear super usuario
    python manage.py createsuperuser


## Primeros pasos

Puedes usar el shell de python para crear estudiantes, exámenes y preguntas o puedes hacerlo desde la consola de Django con el superusuario que creaste en el paso anterior.

Shell Python

    python manage.py shell

    from django.contrib.auth.models import User
    from app_test.models import Student, Test, Question

    user1 = User.objects.create_user('estudiante1', password='password1')
    student1 = Student.objects.create(user=user1)

    test1 = Test.objects.create(title='Test 1', description='Este es el test 1',pub_date='2023-03-08')
    
    question1 = Question.objects.create(test=test1, text='¿Cuál es la capital de Colombia?')

    import requests

    url = 'http://localhost:8000/login/'
    data = {'username': 'estudiante1', 'password': 'password1'}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        token = response.json()['access']
        print(f'Token JWT de acceso: {token}')
    else:
        print('Error al obtener el token JWT de acceso')

    response = requests.post('http://localhost:8000/submit_answers/', headers={'Authorization': 'Bearer <token>'}, json={"test": 1, "answer": "Bolivia", "student": 1, "question": 1})

    

## Documentación Postman

https://documenter.getpostman.com/view/15604060/2s93JtPP75#ceeb1729-281f-4c19-a273-b8cf61add0f8

