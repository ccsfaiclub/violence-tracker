// temp data with both address and long/lat points
const URL = 'https://data.sfgov.org/resource/wr8u-xric.json';
// const URL = 'http://localhost:5000/graphql';

export function getData() {
    return fetch(URL).then(result => result.json());
}

