// temp data with both address and long/lat points
const URL = 'https://data.sfgov.org/resource/wr8u-xric.json';

export function getData() {
    return fetch(URL).then(result => result.json());
}

