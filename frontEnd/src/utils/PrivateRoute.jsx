import React from 'react';
import { Route, Navigate, Router, Routes } from 'react-router-dom';
import { AuthProvider } from '../context/AuthContext'; // Make sure to import the useAuth hook from the correct file path

export default function PrivateRoute({ element: Element, ...rest }) {
	const { isAuthenticated } = AuthProvider(); // Get the isAuthenticated status from the AuthContext or any other way you handle authentication

	return (
		<Route
			{...rest}
			element={
				isAuthenticated ? (
					<Element /> // If the user is authenticated, render the component passed in the `element` prop
				) : (
					<Navigate to='/login' /> // If the user is not authenticated, redirect to the login page (or any other appropriate route)
				)
			}
		/>
	);
}
