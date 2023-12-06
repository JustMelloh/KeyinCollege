// Question 2

import React from 'react';

const Users = ({ users }) => {
    const filterUsers = users.filter(user => user.charAt(0).toUpperCase() === 'B');

    return (
        <div>
            <h1>Names starting with the letter B</h1>
            <ul>
                {filterUsers.map((user, index) => (
                    <li key={index}>{user}</li>
                ))}
            </ul>
        </div>
    );
};

export default Users