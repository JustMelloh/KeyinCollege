// Question 3 Testing

import React from 'react';
import {render, screen, waitFor} from '@testing-library/react';
import HappyHolidays from './HappyHolidays';

jest.useFakeTimers();

test('render HappyHolidays component', () => {
    render(<HappyHolidays />);
    const decemberHeading = screen.getByText(/It's December!!!/i);
    expect(decemberHeading).toBeInTheDocument();
});

test('Dont initialize "Happy Holidays Hurrah!"', () => {
    render(<HappyHolidays />);
    const happyHolidaysHeading = screen.queryByText(/Happy Holidays Hurrah!/i);
    expect(happyHolidaysHeading).not.toBeInTheDocument();
});

test('initialize "Happy Holidays Hurrah!"', async () => {
    render(<HappyHolidays />);
    jest.advanceTimersByTime(3000); 

    await waitFor(() => {
        const happyHolidaysHeading = screen.getByText(/Happy Holidays Hurrah!/i);
        expect(happyHolidaysHeading).toBeInTheDocument();
    });
});