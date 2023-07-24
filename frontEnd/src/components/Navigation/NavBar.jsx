import React from 'react';
import { Link } from 'react-router-dom';

export default function NavBar() {
	const navigation = [
		// {
		// 	to: '/',
		// 	name: 'home',
		// },
		{
			to: 'dashboard',
			name: 'dashboard',
		},
		{
			to: 'messages',
			name: 'messages',
		},

		{
			to: 'statistics',
			name: 'statistics',
		},
		{
			to: 'updates',
			name: 'updates',
		},
		{
			to: 'create',
			name: 'create',
		},
		{
			to: 'login',
			name: 'login',
		},
	];
	return (
		<>
			<div className='navbar bg-base-200 '>
				<div className='navbar-start'>
					<div className='dropdown'>
						<label
							tabIndex={0}
							className='btn btn-ghost lg:hidden'>
							<svg
								xmlns='http://www.w3.org/2000/svg'
								className='h-5 w-5'
								fill='none'
								viewBox='0 0 24 24'
								stroke='currentColor'>
								<path
									strokeLinecap='round'
									strokeLinejoin='round'
									strokeWidth='2'
									d='M4 6h16M4 12h8m-8 6h16'
								/>
							</svg>
						</label>
						<ul
							tabIndex={0}
							className=' menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52'>
							{navigation.map((nav, index) => (
								<li
									key={index}
									className='w-full hover:bg-neutral-focus  rounded-md'>
									<Link
										to={nav.to}
										className='capitalize  px-5  active:bg-neutral-content'>
										{nav.name}
									</Link>
								</li>
							))}
						</ul>
					</div>
					<Link className='btn btn-ghost normal-case text-xl'>
						MailDrop
					</Link>
				</div>

				<div className='navbar-center hidden lg:flex'>
					<ul className=' menu menu-horizontal px-1 flex'>
						{navigation.map((nav, index) => (
							<li
								key={index}
								className='hover:bg-neutral-focus  rounded-md'>
								<Link
									to={nav.to}
									className='capitalize  px-5  active:bg-neutral-content'>
									{nav.name}
								</Link>
							</li>
						))}
					</ul>
				</div>

				<div className='navbar-end'>
					<div className='dropdown dropdown-end'>
						<label
							tabIndex={0}
							className='btn btn-ghost btn-circle avatar placeholder online'>
							<div className='w-10 rounded-full bg-neutral-content text-neutral '>
								{/* <img src='/images/stock/photo-1534528741775-53994a69daeb.jpg' /> */}
								<span className='text-xs'>AA</span>
							</div>
						</label>
						<ul
							tabIndex={0}
							className='menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52'>
							<li>
								<Link
									to={'profile'}
									className='justify-between'>
									Profile
									{/* <span className='badge'>New</span> */}
								</Link>
							</li>
							{/* <li>
								<a>Settings</a>
							</li> */}
							
							{/* <li>
								<Link to={'profile/logout'}>
									Logout
								</Link>
							</li> */}
						</ul>
					</div>
				</div>
				
			</div>
		</>
	);
}
