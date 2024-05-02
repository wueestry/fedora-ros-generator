# Meta Package
Name:           ros-iron-cyclonedds
Version:        0.10.4
Release:        1%{?dist}
License:        Eclipse Public License 2.0
URL:            https://projects.eclipse.org/projects/iot.cyclonedds
Summary:        Meta package for ros2-iron-cyclonedds and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-cyclonedds
Requires:       ros2-iron-cyclonedds-devel

Obsoletes: ros-iron-cyclonedds < 0.10.4-1

%description
Eclipse Cyclone DDS is a very performant and robust open-source DDS
implementation. Cyclone DDS is developed completely in the open as an
Eclipse IoT project.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.10.4-1
- Update to latest release
