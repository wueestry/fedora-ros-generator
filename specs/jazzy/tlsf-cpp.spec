# Meta Package
Name:           ros-jazzy-tlsf-cpp
Version:        0.17.1
Release:        1%{?dist}
License:        GNU Lesser Public License 2.1
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tlsf_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tlsf_cpp
Requires:       ros2-jazzy-tlsf_cpp-devel

Obsoletes: ros-jazzy-tlsf-cpp < 0.17.1-1

%description
C++ stdlib-compatible wrapper around tlsf allocator and ROS2 examples

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
