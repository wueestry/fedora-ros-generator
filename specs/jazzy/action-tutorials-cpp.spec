# Meta Package
Name:           ros-jazzy-action-tutorials-cpp
Version:        0.33.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-action_tutorials_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-action_tutorials_cpp
Requires:       ros2-jazzy-action_tutorials_cpp-devel

Obsoletes: ros-jazzy-action-tutorials-cpp < 0.33.2-1

%description
C++ action tutorial cpp code

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.2-1
- Update to latest release
