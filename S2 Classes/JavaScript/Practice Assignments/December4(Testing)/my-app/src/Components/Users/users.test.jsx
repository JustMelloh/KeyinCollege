// Question 2 Testing

import React from "react";
import {render , screen} from "@testing-library/react";
import Users from "./Users";


const userArray = ['Simon', 'Barbera', 'Bob', 'Elf', 'Alexandar', 'Brad'];

test('renders correct heading text', () => {
    render(<Users  users={userArray}/>);
    const headingElement = screen.getByRole('heading', {name: /Names starting with letter B/i});
    expect(headingElement).toBeInTheDocument();
});

test('renders list of users', () => {
    render(<Users  users={userArray}/>);
    const listElement = screen.getByRole('list');
    expect(listElement).toBeInTheDocument();

});

test(`count users starting with "B"`, () => {
    render(<Users  users={userArray}/>);
    const listItemElements = screen.getAllByRole('listitem');
    expect(listItemElements.length).toBe(3);
});