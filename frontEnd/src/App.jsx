import React, { useEffect, useState } from 'react';
import Navbar from './components/NavBar';
import Stats from './components/Stats';
import Fetch from './Fetch';

export default function App() {
	return (
		<>
			<Navbar />
			<Stats />

			<div>
				<h1>Fetch Example</h1>
				<Fetch
					url='http://127.0.0.1:8000/api/students/'
					options={{
						method: 'GET',
						headers: {
							'Content-Type': 'application/json',
							// Additional headers if required
						},
					}}
					render={({ data, isLoading, error }) => {
						if (isLoading) {
							return <p>Loading...</p>;
						}
						if (error) {
							return <p>Error: {error}</p>;
						}
						if (data) {
							return (
								<ul>
									{data.map((student) => (
										<li key={student.id}>
											<p>
												Program:{' '}
												{student.program}
											</p>
											<p>
												Level:{' '}
												{student.level}
											</p>
											<p>
												Year: {student.year}
											</p>
											<p>
												Index:{' '}
												{student.index}
											</p>
											<p>
												Email:{' '}
												{student.email}
											</p>
										</li>
									))}
								</ul>
							);
						}
						return null;
					}}
				/>
			</div>
		</>
	);
}
