# Meta Package
Name:           ros-jazzy-ruckig
Version:        0.9.2
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ruckig and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ruckig
Requires:       ros2-jazzy-ruckig-devel

Obsoletes: ros-jazzy-ruckig < 0.9.2-1

%description
Instantaneous Motion Generation for Robots and Machines.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.9.2-1
- Update to latest release
