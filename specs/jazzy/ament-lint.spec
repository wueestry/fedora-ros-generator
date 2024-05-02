# Meta Package
Name:           ros-jazzy-ament-lint
Version:        0.17.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_lint and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_lint
Requires:       ros2-jazzy-ament_lint-devel

Obsoletes: ros-jazzy-ament-lint < 0.17.0-1

%description
Providing common API for ament linter packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
