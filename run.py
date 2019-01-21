from app import initialize_app


app = initialize_app()






if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run()
    