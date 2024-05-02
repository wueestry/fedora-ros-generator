# Meta Package
Name:           ros-iron-ament-lint-common
Version:        0.14.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_lint_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_lint_common
Requires:       ros2-iron-ament_lint_common-devel

Obsoletes: ros-iron-ament-lint-common < 0.14.3-1

%description
The list of commonly used linters in the ament build system in CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.14.3-1
- Update to latest release
