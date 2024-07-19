# 3Stack-NFP

![img](https://github.com/AppleBoiy/3Stack-NFP/blob/main/public/docs/system.png?raw=true)

> 3-Tier Architecture for a Next.js, Flask, PostgreSQL

## Getting Started

### Postman Collection

You can use the Postman collection to test the API endpoints.

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/27963483-44986ddb-005e-4db3-ae41-85cf3a4bb8ce?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D27963483-44986ddb-005e-4db3-ae41-85cf3a4bb8ce%26entityType%3Dcollection%26workspaceId%3D22284b4e-23d0-4de8-915a-7190138c12c2)

### Prerequisites

- [Node.js](https://nodejs.org/en/download/)
- [Yarn](https://yarnpkg.com/getting-started/install)
- [Docker](https://docs.docker.com/get-docker/)

### Installation

1. Clone the repository

```bash
git clone git@github.com:AppleBoiy/3Stack-NFP.git
cd 3Stack-NFP
```

### backend and database

> [!IMPORTANT]
> requires docker-compose and Make to be installed

1. use make to start the backend and database

```bash
make build
```

- The backend will be available at [http://localhost:56733](http://localhost:56733)
- The database will be available at [http://localhost:5432](http://localhost:5432)
    - POSTGRES_USER=hello_flask
    - POSTGRES_PASSWORD=hello_flask
    - POSTGRES_DB=hello_flask_dev

### frontend

1. navigate to the frontend directory

```bash
cd next
```

2. Install dependencies

```bash
yarn
```

3. Start the development server

```bash
yarn dev
```

4. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Documentation

see [docs](/docs/readme.md) for more information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details