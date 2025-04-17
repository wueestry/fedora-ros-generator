# Meta Package
Name:           ros-jazzy-ament-cpplint
Version:        0.17.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cpplint and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cpplint
Requires:       ros2-jazzy-ament_cpplint-devel

Obsoletes: ros-jazzy-ament-cpplint < 0.17.2-1

%description
The ability to check code against the Google style conventions using
cpplint and generate xUnit test result files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
