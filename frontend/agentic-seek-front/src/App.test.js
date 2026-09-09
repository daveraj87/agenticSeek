import { render, screen } from '@testing-library/react';
import App from './App';
import { ThemeProvider } from './contexts/ThemeContext';

// react-markdown and axios ship as ESM, which the CRA Jest config does not transform.
jest.mock('react-markdown', () => {
  const React = require('react');
  return ({ children }) => React.createElement('div', null, children);
});
jest.mock('axios', () => ({
  get: jest.fn(() => Promise.resolve({ data: { answer: '', is_active: false } })),
  post: jest.fn(() => Promise.resolve({ data: {} })),
}));

test('renders the Save It Somewhere brand in the header', () => {
  render(
    <ThemeProvider>
      <App />
    </ThemeProvider>
  );
  expect(screen.getByRole('heading', { name: /save it somewhere/i })).toBeInTheDocument();
  expect(screen.getByAltText('Save It Somewhere')).toHaveAttribute(
    'src',
    expect.stringMatching(/\/branding\/svg\/icon(-dark)?\.svg$/)
  );
});
