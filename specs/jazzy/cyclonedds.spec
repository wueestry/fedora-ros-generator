# Meta Package
Name:           ros-jazzy-cyclonedds
Version:        0.10.5
Release:        1%{?dist}
License:        Eclipse Public License 2.0
URL:            https://projects.eclipse.org/projects/iot.cyclonedds
Summary:        Meta package for ros2-jazzy-cyclonedds and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-cyclonedds
Requires:       ros2-jazzy-cyclonedds-devel

Obsoletes: ros-jazzy-cyclonedds < 0.10.5-1

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
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.10.5-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.10.4-1
- Update to latest release
