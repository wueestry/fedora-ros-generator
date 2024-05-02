# Meta Package
Name:           ros-jazzy-ament-pycodestyle
Version:        0.17.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_pycodestyle and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_pycodestyle
Requires:       ros2-jazzy-ament_pycodestyle-devel

Obsoletes: ros-jazzy-ament-pycodestyle < 0.17.0-1

%description
The ability to check code against the style conventions in PEP 8 and
generate xUnit test result files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
