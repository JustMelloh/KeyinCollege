// Question 3 Testing

import React from 'react';
import {render, screen, waitFor, act} from '@testing-library/react'; 
//Added Act to signal to React that it is a status update. This helps ensure the test acts 
//more like it would in a real environ.
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

test('initialize "Happy Holidays Hurrah!"', async () => { // Must make it async due to the await keyword which waits for the time to elapse before passing.
    render(<HappyHolidays />);

    act(() => {
        jest.advanceTimersByTime(3000); // 3000 = 3 Seconds.
      });

    await waitFor(() => {
        const happyHolidaysHeading = screen.getByText(/Happy Holidays Hurrah!/i);
        expect(happyHolidaysHeading).toBeInTheDocument();
    });
});