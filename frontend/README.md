# Frontend Application

This is the frontend part of the application built using React. It provides user interfaces for authentication, community features, and ethical safeguards.

## Project Structure

- **src/**: Contains the source code for the React application.
  - **components/**: Contains reusable components.
    - **Auth/**: Components related to user authentication.
      - **Login.tsx**: Handles user login functionality.
      - **Register.tsx**: Handles user registration functionality.
    - **Community/**: Components related to community features.
      - **CommunityList.tsx**: Displays a list of communities.
      - **CommunityDetail.tsx**: Displays detailed information about a selected community.
    - **Safeguards/**: Components related to ethical safeguards.
      - **EthicalNotice.tsx**: Displays ethical notices and prompts.
  - **pages/**: Contains page components.
    - **Home.tsx**: Home page of the application.
    - **Profile.tsx**: User profile page.
    - **Community.tsx**: Community management page.
  - **types/**: Contains TypeScript types and interfaces.

## Setup Instructions

1. **Install Dependencies**: Navigate to the `frontend` directory and run:
   ```
   npm install
   ```

2. **Run the Application**: Start the development server with:
   ```
   npm start
   ```

3. **Access the Application**: Open your browser and go to `http://localhost:3000` to view the application.

## Features

- **User Authentication**: Users can register and log in to access community features.
- **Community Management**: Users can view and manage community rooms.
- **Ethical Safeguards**: The application includes ethical notices to ensure user consent and data protection.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.