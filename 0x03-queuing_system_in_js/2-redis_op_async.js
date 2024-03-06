import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Promisify the get function of the Redis client
const getAsync = promisify(client.get).bind(client);

// Function to display the value for a given key in Redis
async function displaySchoolValue(schoolName) {
    try {
        // Use await to asynchronously get the value for the key
        const reply = await getAsync(schoolName);
        console.log(reply);
    } catch (error) {
        console.error(error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
