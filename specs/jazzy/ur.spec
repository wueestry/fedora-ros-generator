# Meta Package
Name:           ros-jazzy-ur
Version:        3.2.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ur and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ur
Requires:       ros2-jazzy-ur-devel

Obsoletes: ros-jazzy-ur < 3.2.0-1

%description
Metapackage for universal robots

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.2.0-1
- Update to latest release
