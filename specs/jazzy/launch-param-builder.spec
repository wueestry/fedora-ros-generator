# Meta Package
Name:           ros-jazzy-launch-param-builder
Version:        0.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-launch_param_builder and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-launch_param_builder
Requires:       ros2-jazzy-launch_param_builder-devel

Obsoletes: ros-jazzy-launch-param-builder < 0.1.1-1

%description
Python library for loading parameters in launch files

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.1.1-1
- Update to latest release
