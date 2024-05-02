# Meta Package
Name:           ros-iron-nav2-velocity-smoother
Version:        1.2.7
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav2_velocity_smoother and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav2_velocity_smoother
Requires:       ros2-iron-nav2_velocity_smoother-devel

Obsoletes: ros-iron-nav2-velocity-smoother < 1.2.7-1

%description
Nav2's Output velocity smoother

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
