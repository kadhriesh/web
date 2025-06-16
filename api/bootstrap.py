




if __name__ == "__main__":
    import uvicorn

    from api.controller.employee import app
    uvicorn.run(app, host="")