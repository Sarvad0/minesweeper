class Minesweeper < Formula
  desc "یک بازی کلاسیک Minesweeper"
  homepage "https://github.com/Sarvad0/minesweeper"
  url "https://github.com/Sarvad0/minesweeper/releases/download/v1.0.0/minesweeper.tar.gz"
  version "1.0.0"
  sha256 "5fa4c76f83066d1e2ac938d021bd997ec5607e1a23c5ac58b9045e31ff99e67f"

  def install
    bin.install "minesweeper.py" => "minesweeper"  # تغییر نام فایل به "minesweeper" در زمان نصب
  end
end
