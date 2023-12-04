// Question 1 Testing

import React from 'react';
import { render, screen } from '@testing-library/react';
import Welcome from './Welcome';

test('renders "Click me" button', () => {
  render(<Welcome />);
  const buttonElement = screen.getByText(/Click me/i);
  expect(buttonElement).toBeInTheDocument();
});

test('renders "Welcome" heading', () => {
  render(<Welcome />);
  const welcomeHeadingElement = screen.getByText(/Welcome/i);
  expect(welcomeHeadingElement).toBeInTheDocument();
});

test('renders "Thanks for visiting" heading', () => {
  render(<Welcome />);
  const thanksHeadingElement = screen.getByText(/Thanks for visiting/i);
  expect(thanksHeadingElement).toBeInTheDocument();
});
