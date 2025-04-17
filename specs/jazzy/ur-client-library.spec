# Meta Package
Name:           ros-jazzy-ur-client-library
Version:        1.9.0
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://wiki.ros.org/ur_client_library
Summary:        Meta package for ros2-jazzy-ur_client_library and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ur_client_library
Requires:       ros2-jazzy-ur_client_library-devel

Obsoletes: ros-jazzy-ur-client-library < 1.9.0-1

%description
Standalone C++ library for accessing Universal Robots interfaces. This
has been forked off the ur_robot_driver.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.9.0-1
- Update to latest release
