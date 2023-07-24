import React, { useContext } from 'react';
import AuthContext from '../context/AuthContext';

export default function Home() {
	// let { name } = useContext(AuthContext);
	return (
		<div className='home '>
			<header className='container hero'>
				<div className='min-h-[70vh] flex justify-center items-center flex-col'>
					<div className='caption w-6/12 '>
						<h1 className='text-5xl  font-extrabold'>
							Promote your product to over 1000 student
							with just a click.
						</h1>
						<p className='my-3'>
							Our service give you easy access to sell and
							promote you product and services to stundent
							through email messages.
						</p>
						<div className='button flex gap-3 mt-5'>
							<button className='btn btn-md btn-primary'>
								Sign up
							</button>
							<button className='btn btn-md btn-neutral btn-outline'>
								learn more
							</button>
						</div>
					</div>
				</div>
				{/* <h1>hello {name}</h1> */}
			</header>

			<small className='animate animate-pulse  text-red-500'>
				Logged in user should not have this as a navigation option
			</small>
		</div>
	);
}
