<img src="/static/AppleComputerRainbow.svg" alt="Logo" width="15%"/>

# Apple ID Verification System

This project provides a web interface for checking the validity of Apple IDs. It uses Flask to serve a web application that allows users to verify their credentials, check verification results, manage user accounts (for admins), and export results.

Online Access: [http://8.134.157.203:5001](http://8.134.157.203:5001)

<img src="/static/screenshot_home.jpeg" width="60%" />

<details>
<summary>Screenshots</summary>
<p float="left">
  <img src="/static/screenshot_data.jpg" width="50%" />
  <img src="/static/screenshot_admin.jpg" width="50%" />
</p>
</details>

## Features

- User login and authentication
- Admin interface to manage user quotas and information
- Apple ID verification result checks
- Export verification results to CSV format
- Batch verification of multiple Apple IDs

## Installation

Clone the repository and install the required Python packages:

```bash
git clone https://github.com/kangvcar/AppleIdChecker.git
cd AppleIdChecker
pip install -r requirements.txt
```

## Usage

Run the Flask application with the following command:

```bash
python app.py
```

# Using Docker (recommended)

1. Build the Docker image:

```bash
docker build -t appleid-checker .
```

2. Run the Docker container:

```bash
docker run -d -p 5000:5000 appleid-checker
```

This will start a container in the background, with port 5000 on your local machine mapped to port 5000 on the container running the Flask application.

Access the web application by navigating to `http://localhost:5000` in your web browser.

## Admin Management

The admin interface at `http://localhost:5000/admin` allows for the following administrative tasks:

- Modifying user verification limits
- Viewing all user information
- Creating new users
- Deleting users

## Verification Results

Users can view their verification results on the `my_verification_results.html` page, with options to filter results based on account status (password correct/incorrect, account locked, unknown errors) and download filtered results as a CSV file.

## Contributing

We welcome contributions. If you have suggestions for improving the application, please fork the repository and create a pull request, or open an issue with the tag "enhancement".

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- Thanks to the Flask framework for making web development approachable.
- Appreciation to the Python community for continuous support.

## Contact

- **Project Maintainer:** [Kangvcar](https://github.com/kangvcar)
- **Email:** kangvcar@gmail.com

## Project Status

This project is currently in development. Users and contributors should expect rapid changes and feature improvements.