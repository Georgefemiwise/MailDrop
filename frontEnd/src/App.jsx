import { Routes, Route, Navigate } from 'react-router-dom';
import MainFrame from './layout/MainFrame';
import Home from './pages/Home';
import NoMatch from './pages/NoMatch';
import Statistics from './pages/Statistics';
import CreateStudent from './pages/CreateStudent';
import Updates from './pages/Updates';
import Dashboard from './pages/Dashboard';
import Profile from './pages/profile/Profile';
import Messages from './pages/Messages';

import Logout from './pages/profile/Logout';
import Login from './pages/profile/Login';
// import PrivateRoute from './utils/PrivateRoute';

export default function App() {
	return (
		<>
			<Routes>
				<Route path='/' element={<MainFrame />}>
					<Route path='/' index element={<Home />} />
					<Route path='messages' element={<Messages />}>
						<Route path='edit' />
						<Route path='send' />
						<Route path='create' />
						<Route path='draft' />
						<Route path='delete' />
					</Route>
					<Route path='/login' element={<Login />} />
					<Route path='statistics' element={<Statistics />} />
					<Route path='create' element={<CreateStudent />} />
					<Route path='updates' element={<Updates />} />
					<Route path='dashboard' element={<Dashboard />} />
					<Route path='profile' element={<Profile />} />
					<Route path='logout' element={<Logout />} />
					<Route path='*' element={<NoMatch />} />
				</Route>
			</Routes>
		</>
	);
}
