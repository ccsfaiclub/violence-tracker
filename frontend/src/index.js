import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import ApolloClient from 'apollo-boost'
import { ApolloProvider } from '@apollo/react-hooks';

// Connects React to Apollo client
let _GRAPHQL_HOST = process.env.REACT_APP_GRAPHQL_HOST_URL || 'http://localhost:5001'
const client = new ApolloClient({
    uri: `${_GRAPHQL_HOST}/graphql`
})

ReactDOM.render(
    <React.StrictMode>
        <ApolloProvider client={client}>
            <App />
        </ApolloProvider>
    </React.StrictMode>,
    document.getElementById('root')
);

serviceWorker.unregister();
