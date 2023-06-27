import { useEffect, useState } from 'react';

export default function fetchData(url, options = {}) {
	const [data, setData] = useState(null);
	const [isLoading, setIsLoading] = useState(false);
	const [error, setError] = useState(null);
	const [count, setCount] = useState(0);

	useEffect(() => {
		const fetchDataAsync = async () => {
			setIsLoading(true);

			try {
				const response = await fetch(url, options);
				const jsonData = await response.json();
				setData(jsonData);
				setCount(jsonData.length);
			} catch (error) {
				setError(error.message);
			}

			setIsLoading(false);
		};

		fetchDataAsync();
	}, []);

	return { data, isLoading, error, count };
}
