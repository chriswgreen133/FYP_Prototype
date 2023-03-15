# Final Year Project 

1.  Clone this repository
2.  Download Miniconda and install it, then make new conda environment with python=3.7 with command
    ```bash
    $ conda create --name fyp python=3.7
    $ conda activate fyp
    ```
3.  Now install required packages by running following commands:
    ```bash
    $ pip install -r requirements.txt
    $ pip install flask[async]
    ```
4.  Run the project:
    ```bash
    $ flask run
    ```
You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!
<!-- gunicorn -w 1 -k eventlet --bind localhost:5000 wsgi:app -->