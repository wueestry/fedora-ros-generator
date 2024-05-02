# Meta Package
Name:           ros-jazzy-ament-flake8
Version:        0.17.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_flake8 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_flake8
Requires:       ros2-jazzy-ament_flake8-devel

Obsoletes: ros-jazzy-ament-flake8 < 0.17.0-1

%description
The ability to check code for style and syntax conventions with
flake8.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
