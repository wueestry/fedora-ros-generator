# Meta Package
Name:           ros-jazzy-ament-lint-auto
Version:        0.17.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_lint_auto and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_lint_auto
Requires:       ros2-jazzy-ament_lint_auto-devel

Obsoletes: ros-jazzy-ament-lint-auto < 0.17.1-1

%description
The auto-magic functions for ease to use of the ament linters in
CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
