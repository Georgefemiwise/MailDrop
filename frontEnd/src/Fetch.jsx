import React, { useEffect, useState } from 'react';

export default function Fetch({ url, options, render }) {
	const [data, setData] = useState(null);
	const [isLoading, setIsLoading] = useState(false);
	const [error, setError] = useState(null);

	useEffect(() => {
		const fetchData = async () => {
			setIsLoading(true);

			try {
				const response = await fetch(url, options);
				const jsonData = await response.json();
				setData(jsonData);
				setIsLoading(false);
			} catch (error) {
				setError(error);
				setIsLoading(false);
			}
		};

		fetchData();
	}, [url, options]);

	return render({ data, isLoading, error });
}
