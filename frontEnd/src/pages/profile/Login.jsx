import React from 'react';

export default function Login() {
	return (
		<div>
			<form>
				<input className='input block mt-2' type='text' name='username' placeholder='enter username' />
				<input className='input block mt-2' type='password' name='password' id='password' placeholder='enter password' />
				<input className='btn btn-success mt-2' type='submit' value='Login' />
			</form>
		</div>
	);
}
