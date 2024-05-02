# Meta Package
Name:           ros-jazzy-ament-clang-format
Version:        0.17.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_clang_format and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_clang_format
Requires:       ros2-jazzy-ament_clang_format-devel

Obsoletes: ros-jazzy-ament-clang-format < 0.17.0-1

%description
The ability to check code against style conventions using clang-format
and generate xUnit test result files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
