import React from 'react';
import { Link } from 'react-router-dom';

export default function NavBar() {
	return (
		<nav className='navbar flex items-start  h-full'>
			<ul className=' text-black font-sembold items-start flex-col '>
				<li>
					<Link to='/'>Home</Link>
				</li>
				<li>
					<Link to='dashboard'>Dashboard</Link>
				</li>
				<li>
					<Link to='statistics'>Stats</Link>
				</li>
				<li>
					<Link to='updates'>Updates</Link>
				</li>
				<li>
					<Link to='create'>Compose</Link>
				</li>
			</ul>
		</nav>
	);
}
