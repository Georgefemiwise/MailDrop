
import { Routes, Route} from 'react-router-dom';
import MainFrame from './layout/MainFrame';
import Home from './pages/Home';
import NoMatch from './pages/NoMatch';
import Statistics from './pages/Statistics';
import CreateStudent from './pages/CreateStudent';
import Updates from './pages/Updates';
import Dashboard from './pages/Dashboard';

export default function App() {
	return (
		<>
			<Routes>
				<Route path='/' element={<MainFrame />}>
					<Route index element={<Home />} />
					<Route path='statistics' element={<Statistics />} />
					<Route path='create' element={<CreateStudent />} />
					<Route path='updates' element={<Updates />} />
					<Route path='dashboard' element={<Dashboard />} />
					<Route path='*' element={<NoMatch />} />
				</Route>
			</Routes>
		</>
	);
}
