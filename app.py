# main components of our app 

from myapp import app #importing from  __init__.py 

if __name__ == '__main__':
    print('Trailist is running')
    app.run(debug=True)