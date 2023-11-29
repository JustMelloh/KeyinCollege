import { render, screen} from "@testing-library/react";
import Header from "../components/Header";

test("My First Test", () => {
    render(<Header />);
    const linkElement = screen.getByText(/keyin college/i);
    expect(linkElement).toBeInDocument();
});