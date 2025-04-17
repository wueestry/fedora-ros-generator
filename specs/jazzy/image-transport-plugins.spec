# Meta Package
Name:           ros-jazzy-image-transport-plugins
Version:        4.0.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/image_transport_plugins
Summary:        Meta package for ros2-jazzy-image_transport_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-image_transport_plugins
Requires:       ros2-jazzy-image_transport_plugins-devel

Obsoletes: ros-jazzy-image-transport-plugins < 4.0.4-1

%description
A set of plugins for publishing and subscribing to sensor_msgs/Image
topics in representations other than raw pixel data. For example, for
viewing a stream of images off-robot, a video codec will give much
lower bandwidth and latency. For low frame rate tranport of high-
definition images, you might prefer sending them as JPEG or PNG-
compressed form.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Mar 14 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.4-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.3-1
- Update to latest release
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.2-1
- Update to latest release
